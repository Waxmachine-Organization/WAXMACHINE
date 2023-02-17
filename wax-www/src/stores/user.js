import { writable } from 'svelte/store';
import { rpc } from '../lib/rpc';
import { goto } from '$app/navigation';

export const sessionId = new writable(
	typeof localStorage !== 'undefined' ? localStorage.getItem('sessionId') : null
);

export const user = new writable();
export const equipment = new writable();

export const fetchUser = async (sessionId) => {
	const { result, error } = await rpc.getUser(sessionId);
	if (error) {
		throw new Error(error);
	}
	return result;
};

export const fetchEquipment = async (sessionId) => {
	const { result, error } = await rpc.getEquipment(sessionId);
	if (error) {
		throw new Error(error);
	}
	return result;
};

export const ensureUser = async (_sessionId, _user, _equipment) => {
	if (!_sessionId) {
		goto('/');
	}
	if (!_user) {
		user.set(await fetchUser(_sessionId));
	}
	if (!_equipment) {
		equipment.set(await fetchEquipment(_sessionId));
	}
};
