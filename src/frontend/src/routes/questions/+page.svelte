<script>
	import { onMount } from 'svelte';
	import { append } from 'svelte/internal';

	let dataq = [];
	let replyData = '';

	onMount(async () => {
		document.getElementById('ques').style.backgroundColor = 'var(--highlight-main)';

		const data = await fetch('/api/questions');
		dataq = await data.json();
	});

	function clickDel(key) {
		fetch(`/api/questions?key=${key}`, { method: 'DELETE' }).then(() => {
			window.location.reload();
		});
	}

	function clickVis(state, key) {
		let pushState = '';
		if (state === true) {
			pushState = false;
		} else {
			pushState = true;
		}
		fetch(`/api/questions?key=${key}`, {
			method: 'PATCH',
			headers: {
				'Content-type': 'application/json'
			},
			body: JSON.stringify({ hidden: pushState })
		}).then(() => {
			window.location.reload();
		});
	}

	function clickResp(key) {
		fetch(`/api/questions?key=${key}`, {
			method: 'PATCH',
			headers: {
				'Content-type': 'application/json'
			},
			body: JSON.stringify({ reply: 'Hi!!', replied: true })
		}).then(() => {
			window.location.reload();
		});
	}
</script>

<nav>
	<div class="nav-items">
		<div class="nav-ele" id="dash"><a href="/dashboard">Dashboard</a></div>
		<div class="nav-sep">/</div>
		<div class="nav-ele" id="ques"><a href="/questions">Questions</a></div>
	</div>
</nav>

<div class="questions">
	{#each dataq as item}
		<div class="question">
			<div class="text">
				{item['question']}
			</div>
			<div class="control">
				{#if item['reply']}
					<input
						type="text"
						class="reply"
						placeholder="Type reply here"
						maxlength="100"
						on:keypress={() => {
							console.log(self);
							item.append({ value: self.value });
						}}
						value={item['reply']}
					/>
				{:else}
					<input
						type="text"
						class="reply"
						placeholder="Type reply here"
						maxlength="100"
						on:keypress={() => {
							item.append({ value: self.value });
						}}
					/>
				{/if}
				<!-- svelte-ignore a11y-click-events-have-key-events -->
				<div class="button send" on:click={clickResp(item['key'])}>
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
				<!-- svelte-ignore a11y-click-events-have-key-events -->
				<div class="button" on:click={clickVis(item['hidden'], item['key'])}>
					{#if item['hidden']}
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
							class="feather feather-eye"
							><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z" /><circle
								cx="12"
								cy="12"
								r="3"
							/></svg
						>
					{:else}
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
							class="feather feather-eye-off"
							><path
								d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"
							/><line x1="1" y1="1" x2="23" y2="23" /></svg
						>
					{/if}
				</div>
				<!-- svelte-ignore a11y-click-events-have-key-events -->
				<div class="button" on:click={clickDel(item['key'])}>
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
						class="feather feather-trash-2"
						><polyline points="3 6 5 6 21 6" /><path
							d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"
						/><line x1="10" y1="11" x2="10" y2="17" /><line x1="14" y1="11" x2="14" y2="17" /></svg
					>
				</div>
			</div>
		</div>
	{/each}
</div>

<style>
	.questions {
		flex-direction: column;
		display: flex;
		justify-content: center;
		align-items: center;
	}

	.question {
		background-color: var(--back-sec);
		padding: 8px 12px;
		border-radius: 4px;
		margin: 10px;
		width: 90vw;
		border: 1px solid var(--text-light);
	}

	.reply {
		background-color: transparent;
		border: 1px solid var(--highlight-main);
		animation: fadeIn 2s;
		text-align: center;
		border-radius: 4px;
		padding: 1px 2px;
		color: var(--text-light);
		background-color: var(--highlight-sec);
	}

	.reply:focus {
		border-color: var(--text-sec);
		color: var(--text-main);
		outline: none;
	}

	.text {
		overflow-wrap: break-word;
		font-size: 20px;
	}

	.control {
		flex-direction: row;
		display: flex;
		gap: 4px;
		margin: 5px;
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
	}

	.button:hover {
		border-color: var(--text-sec);
		color: var(--text-main);
	}

	svg {
		height: 15px;
		width: 15px;
	}

	/* View */

	/*
	@media only screen and (min-width: 1200px) {
		.question {
			padding: 20px 40px;
		}

		.text {
			font-size: 40px;
		}

		.reply {
			padding: 10px 80px;
		}

		.button {
			padding: 10px 20px;
		}
	}
	*/
</style>
