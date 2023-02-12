<script>
	import { onMount } from 'svelte';

	let mainData = [];
	let displayName = '';
	let displayImg = '';
	let subState = '';

	onMount(async () => {
		const data = await fetch('/api/public');
		mainData = await data.json();

		try {
			displayName = mainData['display_name']['value'];
			displayImg = mainData['display_image']['value'];
			subState = mainData['submissions_state']['value'];
		} catch {}

		const answeredBtn = document.getElementById('answered');
		const questionData = document.getElementById('question');

		answeredBtn.addEventListener('click', () => {
			window.location.href = `/answered`;
		});
	});

	function clickSend() {
		if (questionData.value === '') {
			questionData.placeholder = `Please enter a question`;
			setTimeout(() => {
				questionData.placeholder = `Ask your question here`;
			}, 800);
			return;
		}
		fetch(`/api/questions?question=${questionData.value}`, { method: 'POST' }).then(
			(questionData.value = ``)
		);
	}
</script>

<div>
	<img src={displayImg} alt="profile" class="picture" />
	<div class="name">Ask {displayName}</div>
	<div class="asking">
		<input
			type="text"
			class="question"
			id="question"
			placeholder="Ask your question here"
			maxlength="100"
		/>
		<button id="send" class="button" on:click={clickSend}>
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
		</button>
	</div>
	<button class="button as" id="answered">Answered Questions</button>
</div>

<style>
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
