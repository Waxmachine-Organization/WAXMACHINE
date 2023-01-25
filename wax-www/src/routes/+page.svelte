<script>
	import { Button } from 'flowbite-svelte';
</script>

<div class="body">
	<div class="bg" />
	<Button color="dark" href="/start">Start Waxing</Button>
</div>

<style>
	.body {
		min-height: 100%;
		display: flex;
		align-items: center;
		justify-content: center;
		position: relative;
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
