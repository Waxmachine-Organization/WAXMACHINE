import { json } from '@sveltejs/kit';
import { loginUser, getEquipment, getUser } from '../../lib/db';
import { createUser, registerEquipment } from '../../lib/db';

const methods = { loginUser, getEquipment, getUser, createUser, registerEquipment };

/** @type {import('@sveltejs/kit').RequestHandler} */
export const POST = async (event) => {
	const { args, method } = await event.request.json();
	let result, error;
	try {
		result = await methods[method](...args);
	} catch (err) {
		error = err.message || err.toString();
	}
	return json({ result, error });
};
