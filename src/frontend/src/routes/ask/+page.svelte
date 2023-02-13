<script>
	import { onMount } from 'svelte';

	let mainData = [];
	let displayName = '';
	let displayImg = '';
	let subState = '';

	let questionData = '';

	onMount(async () => {
		const data = await fetch('/api/public/config');
		mainData = await data.json();
		try {
			displayName = mainData['display_name']['value'];
			displayImg = mainData['display_image']['value'];
			subState = mainData['submissions_state']['value'];
		} catch {}
	});

	function clickAns() {
		window.location.href = `/answered`;
	}

	function clickSend() {
		if (questionData === '') {
			questionData = `Please enter a question`;
			setTimeout(() => {
				questionData = ``;
			}, 800);
			return;
		}
		fetch(`/api/questions?question=${questionData}`, { method: 'POST' }).then((questionData = ``));
	}
</script>

<div class="ask">
	{#if subState}
		<img src={displayImg} alt="profile" class="picture" />
		<div class="name">Ask {displayName}</div>
		<div class="asking">
			<input
				type="text"
				class="question"
				id="question"
				placeholder="Ask your question here"
				maxlength="100"
				bind:value={questionData}
			/>
			<!-- svelte-ignore a11y-click-events-have-key-events -->
			<div id="send" class="button" on:click={clickSend}>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					width="24"
					height="24"
					viewBox="0 0 24 24"
					fill="none"
					stroke="currentColor"
					stroke-width="2"
					stroke-linecap="round"
					stroke-linejoin="round"
					class="feather feather-send"
				>
					<line x1="22" y1="2" x2="11" y2="13" />
					<polygon points="22 2 15 22 11 13 2 9 22 2" />
				</svg>
			</div>
		</div>
		<!-- svelte-ignore a11y-click-events-have-key-events -->
		<div class="button as" on:click={clickAns}>Answered Questions</div>
		<div class="info">
			Built with <a href="https://deta.space/discovery/@sofa/askme">AskMe</a>, powered by
			<a href="https://deta.space">Deta Space</a>
		</div>
	{:else}
		<div class="message">
			{displayName} is currently not answering new questions!
		</div>
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

	.asking {
		flex-direction: row;
		display: flex;
		align-items: center;
	}

	.name {
		font-size: 50px;
		color: var(--text-dark);
		margin: 5px;
	}

	.picture {
		border-radius: 50%;
		height: 140px;
		width: 140px;
	}

	.button {
		padding: 4px 8px;
		border: 1px solid var(--highlight-main);
		border-radius: 4px;
		background-color: var(--highlight-sec);
		cursor: pointer;
		color: var(--text-light);
		justify-content: center;
		align-items: center;
		font-size: 10px;
		align-self: center;
		margin: 10px;
	}

	.button:hover {
		border-color: var(--text-sec);
		color: var(--text-main);
	}

	.button.as {
		font-size: 15px;
	}

	.question {
		padding: 6px 20px;
		border-radius: 4px;
		text-align: center;
		border: 1px solid var(--highlight-main);
		background-color: var(--highlight-sec);
		width: 150px;
	}

	.question:focus {
		border-color: var(--text-sec);
		color: var(--text-main);
		outline: none;
	}

	svg {
		height: 15px;
		width: 15px;
	}
</style>
