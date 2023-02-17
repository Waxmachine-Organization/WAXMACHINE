const rpcCall =
	(method) =>
	async (...args) => {
		const res = await fetch('/rpc', {
			method: 'POST',
			body: JSON.stringify({ args, method }),
			headers: { 'content-type': 'application/json' }
		});
		const json = await res.json();
		return json;
	};

const methods = ['loginUser', 'getEquipment', 'getUser', 'createUser', 'registerEquipment'];

export const rpc = Object.fromEntries(methods.map((method) => [method, rpcCall(method)]));
