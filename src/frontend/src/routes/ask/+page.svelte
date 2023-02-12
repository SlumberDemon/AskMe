<script>
	import { onMount } from 'svelte';
	import Ask from '../../components/Ask.Svelte';

	let mainData = [];
	let displayName = '';
	let subState = '';

	onMount(async () => {
		const data = await fetch('/api/public');
		mainData = await data.json();

		try {
			displayName = mainData['display_name']['value'];
			subState = mainData['submissions_state']['value'];
		} catch {}
	});
</script>

<div class="ask">
	{#if subState}
		<Ask />
		<div class="info">
			Built with <a href="https://deta.space/discovery/@sofa/askme">AskMe</a>, powered by
			<a href="https://deta.space">Deta Space</a>
		</div>
	{:else}
		<div class="message">{displayName} is currently not answering new questions!</div>
	{/if}
</div>

<style>
	.ask {
		margin: 10px;
		display: flex;
		align-items: center;
		justify-content: center;
		flex-direction: column;
	}

	.info {
		margin: 10px;
		position: fixed;
		bottom: 0;
	}

	/*
	#blur {
		filter: blur(5px);
	}
	*/
</style>
