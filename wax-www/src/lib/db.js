import { MongoClient } from 'mongodb';
import { config } from 'dotenv';
import { createHash, randomBytes } from 'crypto';

const hash = (password) => createHash('sha256').update(password).digest().toString('hex');
const createSessionId = (n = 32) => Buffer.from(randomBytes(n)).toString('hex');

config();

let client;

export const getDb = async () => {
	if (!client) {
		client = new MongoClient(process.env.DB_URI);
		await client.connect();
	}

	return client.db(process.env.DB_NAME);
};

export const getUser = async (sessionId) => {
	const db = await getDb();
	const users = db.collection('users');
	return await users.findOne({ sessionId });
};

export const loginUser = async (email, password) => {
	const db = await getDb();
	const users = db.collection('users');
	const sessionId = createSessionId();
	const update = await users.updateOne(
		{ email, password: hash(password) },
		{ $push: { sessionId } }
	);
	return { update, sessionId };
};

export const createUser = async (email, password) => {
	const db = await getDb();
	const users = db.collection('users');
	if (await users.findOne({ email })) {
		throw new Error('Email already in use');
	}
	const sessionId = createSessionId();
	const insert = await users.insertOne({ email, password: hash(password), sessionId: [sessionId] });
	return { insert, sessionId };
};

export const registerEquipment = async (equipment) => {
	const db = await getDb();
	const equipments = db.collection('equipments');
	return await equipments.insertOne(equipment);
};

export const getEquipment = async (sessionId) => {
	const db = await getDb();
	const equipments = db.collection('equipments');
	const { _id } = await getUser(sessionId);
	return await equipments.find({ userId: _id.toString() }).toArray();
};
