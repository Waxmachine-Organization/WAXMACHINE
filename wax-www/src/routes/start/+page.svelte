<script>
	import { Button } from 'flowbite-svelte';
	import { goto } from '$app/navigation';

	const unlock = async () => {
		await fetch('https://wax.eu.ngrok.io/unlock');
		goto('/process');
	};
</script>

<div class="body">
	<div class="bg" />
	<Button color="dark" on:click={unlock}>Unlock Machine</Button>
</div>

<style>
	.body {
		min-height: 100%;
		display: flex;
		align-items: center;
		justify-content: center;
	}
	.bg {
		position: absolute;
		left: 0;
		right: 0;
		top: 0;
		bottom: 0;
		background: url(/images/bg2.jpeg);
		background-position: center center;
		background-size: cover;
		opacity: 0.25;
		z-index: -1;
	}
</style>
