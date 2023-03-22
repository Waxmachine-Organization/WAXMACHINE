<script>
	import { Button, ButtonGroup } from 'flowbite-svelte';
	import { Input, Label } from 'flowbite-svelte';

	import { sessionId, ensureUser } from '../stores/user';
	import { rpc } from '../lib/rpc';
	import { goto } from '$app/navigation';
	import { _ } from 'svelte-i18n';
	import toast from 'svelte-french-toast';

	let email;
	let password;

	const validate = () => {
		if (!email) {
			toast.error('Email is required');
			return false;
		}
		if (!email.match(/^.+@.+\..+$/)) {
			toast.error('Email is not valid');
			return false;
		}
		if (!password) {
			toast.error('Password is required');
			return false;
		}
		if (password.length < 8) {
			toast.error('Password should be minimum 8 characters');
			return false;
		}
		return true;
	};

	const userAlreadyLoggedIn = async () => {
		await ensureUser($sessionId);
		goto('/wax');
	};

	const userSignIn = async () => {
		if (!validate()) return;
		const { error, result } = await rpc.loginUser(email, password);
		if (error) {
			return toast.error(error.message || error);
		}
		if (!result.update.modifiedCount) {
			return toast.error("User doesn't exist");
		}
		localStorage.setItem('sessionId', result.sessionId);
		$sessionId = result.sessionId;
		userAlreadyLoggedIn();
	};

	const userSignUp = async () => {
		if (!validate()) return;
		const { error, result } = await rpc.createUser(email, password);
		if (error) {
			return toast.error(error.message || error);
		}
		localStorage.setItem('sessionId', result.sessionId);
		$sessionId = result.sessionId;
		userAlreadyLoggedIn();
	};

	if ($sessionId) {
		userAlreadyLoggedIn();
	}
</script>

<div class="body">
	<div class="bg" />
	<div class="mb-6">
		<Label for="email" class="mb-2">Email</Label>
		<Input bind:value={email} type="email" id="email" placeholder="john.doe@company.com" required />
	</div>
	<div class="mb-6">
		<Label for="password" class="mb-2">{$_('password')}</Label>
		<Input bind:value={password} type="password" id="password" placeholder="•••••••••" required />
	</div>
	<div class="mb-6">
		<ButtonGroup>
			<Button color="blue" size="md" on:click={userSignIn}>{$_('signIn')}</Button>
			<Button color="alternative" size="md" on:click={userSignUp}>{$_('signUp')}</Button>
		</ButtonGroup>
	</div>
	<div>
	    <p>{$_('instructionsRegister')}</p>
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
		background: url(/images/bg1.jpeg);
		background-position: center center;
		background-size: cover;
		opacity: 0.25;
		z-index: -1;
	}
</style>
