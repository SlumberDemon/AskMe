<script>
	import { onMount } from 'svelte';

	let mainData = [];

	onMount(async () => {
		questionData = document.getElementById('question');

		const data = await fetch('/api/public');
		mainData = await data.json();

		const answeredBtn = document.getElementById('answered');

		answeredBtn.addEventListener('click', () => {
			window.location.href = `/answered`;
		});
	});

	function sendBtn() {
		if (questionData.value === '') {
			questionData.placeholder = `Please enter a question`;
			setTimeout(() => {
				questionData.placeholder = `Ask your question here`;
			}, 800);
			return;
		}
		questionData.value = ``;
	}
</script>

<div class="ask">
	{#if mainData['submissions_state']['value']}
		<img src={mainData['display_image']['value']} alt="profile" class="picture" />
		<div class="name">Ask {mainData['display_name']['value']}</div>
		<div class="asking">
			<input
				type="text"
				class="question"
				id="question"
				placeholder="Ask your question here"
				maxlength="100"
			/>
			<!-- svelte-ignore a11y-click-events-have-key-events -->
			<div id="send" class="button" on:click={sendBtn}>
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
		<div class="button as" id="answered">Answered Questions</div>
		<div class="info">
			Built with <a href="https://deta.space/discovery/@sofa/askme">AskMe</a>, powered by
			<a href="https://deta.space">Deta Space</a>
		</div>
	{:else}
		<div class="message">
			{mainData['display_name']['value']} is currently not answering new questions!
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

	.info {
		margin: 10px;
		position: fixed;
		bottom: 0;
	}

	svg {
		height: 15px;
		width: 15px;
	}

	/*
	#blur {
		filter: blur(5px);
	}
	*/
</style>
