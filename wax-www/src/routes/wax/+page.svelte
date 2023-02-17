<script>
	import { Button } from 'flowbite-svelte';
	import { ensureUser } from '../../stores/user';
	import { onMount } from 'svelte';
	import { sessionId, equipment } from '../../stores/user';
	import { goto } from '$app/navigation';
	import toast from 'svelte-french-toast';
	import { _ } from 'svelte-i18n';

	const start = () => {
		if (!$equipment.length) {
			return toast.error(_('registerFirst'));
		}
		goto('/start');
	};

	onMount(async () => {
		await ensureUser($sessionId);
	});
</script>

<div class="body">
	<div class="bg" />
	<Button color="dark" on:click={start}>{$_('start')}</Button>
	<Button color="dark" href="/register">{$_('registerEquipment')}</Button>
</div>

<style>
	.body {
		min-height: 100%;
		display: flex;
		align-items: center;
		justify-content: center;
		position: relative;
		gap: 1em;
		flex-direction: column;
	}
	.bg {
		position: absolute;
		left: 0;
		right: 0;
		top: 0;
		bottom: 0;
		background: url(/images/bg1.jpeg);
		background-position: center center;
		background-size: cover;
		opacity: 0.25;
		z-index: -1;
	}
</style>
