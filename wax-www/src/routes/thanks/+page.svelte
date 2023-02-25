<script>
	import { Button } from 'flowbite-svelte';
	import { _ } from 'svelte-i18n';
</script>

<div class="body">
	<div class="bg" />
	<div class="message">
		<h1>{$_('thanks')}</h1>
		<p>
			{$_('feedback')}
		</p>
	</div>
	<Button color="green" href="https://forms.gle/zR5vuTXjYmsvsahX7">{$_('giveFeedback')}</Button>
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
