<script>
	import { Button } from 'flowbite-svelte';
	import { goto } from '$app/navigation';

	const lock = async () => {
		await fetch('https://wax.eu.ngrok.io/end');
		goto('/thanks');
	};
</script>

<div class="body">
	<div class="bg" />
	<div class="message">
		<h1>Waxing done!</h1>
		<p>The door is unlocked, you can open it and pick up your equipment.</p>
		<p>Then close the door and</p>
	</div>
	<Button color="red" on:click={lock}>Lock back the machine</Button>
</div>

<style>
	.body {
		min-height: 100%;
		display: flex;
		align-items: center;
		justify-content: center;
		flex-direction: column;
		gap: 2em;
		padding: 2em;
		box-sizing: border-box;
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
	h1 {
		font-size: 1.4em;
		margin-bottom: 1em;
	}
	.message {
		text-align: center;
		font-size: 1.1em;
	}
</style>
