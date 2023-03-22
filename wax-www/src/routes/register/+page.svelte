<script>
	import { Button, ButtonGroup } from 'flowbite-svelte';
	import { ensureUser } from '../../stores/user';
	import { onMount } from 'svelte';
	import { sessionId, user, equipment } from '../../stores/user';
	import { Input, Label } from 'flowbite-svelte';
	import { rpc } from '../../lib/rpc';
	import { _ } from 'svelte-i18n';

	import toast from 'svelte-french-toast';

	let brand, model, size;

	const validate = () => {
		if (!brand) {
			toast.error('Brand is required');
			return false;
		}
		if (!model) {
			toast.error('Model is required');
			return false;
		}
		if (!size) {
			toast.error('Size is required');
			return false;
		}
		return true;
	};

	const back = () => {
		history.back();
	};

	const register = async () => {
		if (!validate()) return;
		const { error } = await rpc.registerEquipment({
			brand,
			model,
			size,
			userId: $user._id
		});
		if (error) {
			return toast.error(error.message || error);
		}
		$equipment = [...$equipment, { brand, model, size }];
		back();
	};

	onMount(async () => {
		await ensureUser($sessionId);
	});
</script>

<div class="body">
	<div class="bg" />
	<div class="mb-6">
		<Label for="email" class="mb-2">{$_('brand')}</Label>
		<Input bind:value={brand} type="text" id="text" placeholder={$_('brand')} required />
	</div>
	<div class="bg" />
	<div class="mb-6">
		<Label for="email" class="mb-2">{$_('model')}</Label>
		<Input bind:value={model} type="text" id="text" placeholder={$_('model')} required />
	</div>
	<div class="bg" />
	<div class="mb-6">
		<Label for="email" class="mb-2">{$_('size')}</Label>
		<Input bind:value={size} type="text" id="text" placeholder={$_('size')} required />
	</div>
	<div class="mb-6">
		<ButtonGroup>
			<Button color="alternative" size="md" on:click={back}>{$_('cancel')}</Button>
			<Button color="blue" size="md" on:click={register}>{$_('register')}</Button>
		</ButtonGroup>
	</div>
</div>

<style>
	.body {
		min-height: 100%;
		display: flex;
		align-items: center;
		justify-content: center;
		position: relative;
		flex-direction: column;
	}
	.bg {
		position: absolute;
		left: 0;
		right: 0;
		top: 0;
		bottom: 0;
		background: url(/images/bg3.jpeg);
		background-position: center center;
		background-size: cover;
		opacity: 0.25;
		z-index: -1;
	}
</style>
