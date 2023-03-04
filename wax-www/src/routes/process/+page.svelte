<script>
	import { Button, Progressbar } from 'flowbite-svelte';
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { ensureUser, sessionId } from '../../stores/user';
	import { wax } from '../../lib/wax';
	import { _ } from 'svelte-i18n';

	let progress = 0;
	let started = 0;
	let interval;
	let start;

	const PROCESS_DURATION = 270000; // 270 secondes

	const begin = async () => {
		await wax.begin();
		started = true;
		start = new Date();
		interval = setInterval(() => {
			const millis = new Date().valueOf() - start.valueOf();
			progress = Math.min(Math.floor(millis / (PROCESS_DURATION / 100)), 100);
		}, 1000);
	};

	const cancel = async () => {
		await wax.cancel();
		goto('/thanks');
	};

	onMount(async () => {
		await ensureUser($sessionId);
		return () => {
			clearInterval(interval);
		};
	});

	$: if (progress === 100) {
		goto('/done');
	}
</script>

<div class="body">
	<div class="bg" />
	<Progressbar color="green" {progress} />
	{#if started}
		<Button on:click={cancel} color="red">{$_('cancel')}</Button>
	{:else}
		<video width="170" height="500" autoplay loop>
			<source src="https://github.com/Waxmachine-Organization/WAXMACHINE/blob/main/wax-www/static/videos/WAX1.mp4?raw=true" type="video/mp4">
		</video>
		<ol class="list-decimal">
			<li>{$_('instructions.3')}</li>
			<li>{$_('instructions.4')}</li>
			<li>{$_('instructions.5')}</li>
		</ol>
		<Button color="dark" on:click={begin}>{$_('begin')}</Button>
	{/if}
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
</style>
