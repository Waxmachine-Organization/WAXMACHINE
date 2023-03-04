const fetchEndpoint = (endpoint) => async () => {
	const res = await fetch(`https://wax.eu.ngrok.io/${endpoint}`);
	return res.ok;
};

const endpoints = [
	'unlock',
	'begin',
	'end',
	'up',
	'down',
	'stop',
	'open',
	'close',
	'isFree',
	'isTimeFree',
	'readIsopropanol',
	'readIntTemp',
	'readExtTemp',
	'readPyro',
	'logs'
];

export const wax = Object.fromEntries(
	endpoints.map((endpoint) => [endpoint, fetchEndpoint(endpoint.toLowerCase())])
);

wax.isOnline = async () => {
	const res = await fetch(`https://wax.eu.ngrok.io`);
	return res.ok;
};
