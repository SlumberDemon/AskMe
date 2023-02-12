<script>
	import { onMount } from 'svelte';

	let route = '';

	onMount(() => {
		route = window.location.route;
	});

	const repliedState = true;
</script>

<div class="answered">
	<div class="card">
		<div class="title">Question | IDHERE</div>
		<div class="question">
			<div class="text ques">
				adgjnadgjkadgkbakdhgbhadbgkhabdghkbadkgbakjdgbkjadbgjkabdgkjbadgbakdgbkajdgbkjadbgkjabdgkjabdkgjbadj
			</div>
		</div>
		<div class="answer">
			<div class="text ans">
				{#if repliedState}
					adgjnadgjkadgkbakdhgbhadbgkhabdghkbadkgbakjdgbkjadbgjkabdgkjbadgbakdgbkajdgbkjadbgkjabdgkjabdkgjbadj
				{:else}
					This question has not been answered!
				{/if}
			</div>
		</div>
	</div>
</div>

<style>
	.answered {
		flex-direction: column;
		align-items: center;
		justify-content: center;
		display: flex;
	}

	.card {
		border: 1px solid;
		border-radius: 4px;
		border: 1px solid var(--text-light);
	}

	.title {
		font-size: 25px;
		margin: 10px;
	}

	.question {
		border: 2px solid var(--highlight-main);
		background-color: var(--highlight-main);
		border-radius: 4px 4px 0px 0px;
		color: var(--text-main);
		padding: 6px 0px;
		width: 90vw;
		overflow-wrap: break-word;
		text-align: center;
		/* backdrop-filter: blur(2px); */
	}

	.answer {
		border: 2px solid var(--highlight-sec);
		background-color: var(--highlight-sec);
		border-radius: 0px 0px 4px 4px;
		color: var(--text-main);
		padding: 6px 0px;
		width: 90vw;
		overflow-wrap: break-word;
		text-align: center;
		/* backdrop-filter: blur(2px); */
	}

	.text {
		color: text(--text-light) !important;
		margin: 5px;
	}
</style>
