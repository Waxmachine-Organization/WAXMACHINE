<script>
	import { Button } from 'flowbite-svelte';
	import { goto } from '$app/navigation';
	import { wax } from '../../lib/wax';
	import { _ } from 'svelte-i18n';

	import { ensureUser, sessionId } from '../../stores/user';
	import { onMount } from 'svelte';

	onMount(async () => {
		await ensureUser($sessionId);
	});

	const unlock = async () => {
		await wax.unlock();
		goto('/process');
	};
</script>

<div class="body">
	<div class="bg" />
	<h2 class="text-xl">{$_('instructions')}</h2>
	<ol class="list-decimal">
		<li>{$_('instructions.1')}</li>
		<li>{$_('instructions.2')}</li>
		<li>{$_('instructions.3')}</li>
		<li>{$_('instructions.4')}</li>
		<li>{$_('instructions.5')}</li>
	</ol>
	<Button color="dark" on:click={unlock}>{$_('unlock')}</Button>
</div>

<style>
	.body {
		min-height: 100%;
		display: flex;
		align-items: center;
		justify-content: center;
		flex-direction: column;
		gap: 2em;
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
