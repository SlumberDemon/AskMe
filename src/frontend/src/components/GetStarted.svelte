<script>
	function start() {
		fetch(`/api/config`, {
			method: 'POST',
			headers: {
				'Content-type': 'application/json'
			},
			body: JSON.stringify({ value: false, key: 'user_state' })
		});
		fetch(`/api/config`, {
			method: 'POST',
			headers: {
				'Content-type': 'application/json'
			},
			body: JSON.stringify({ value: false, key: 'submissions_state' })
		});
		fetch(`/api/config`, {
			method: 'POST',
			headers: {
				'Content-type': 'application/json'
			},
			body: JSON.stringify({ value: '', key: 'display_name' })
		});
		fetch(`/api/config`, {
			method: 'POST',
			headers: {
				'Content-type': 'application/json'
			},
			body: JSON.stringify({ value: '', key: 'display_image' })
		});
		window.location.href = `/dashboard`;
	}
</script>

<div class="main">
	<div class="title">AskMe</div>
	<div class="sub-title">The anonymous q&a app</div>
	<div class="instructions">
		<div class="t-inst">Dashboard:</div>
		<div class="t-ele">1. Enter a display name</div>
		<div class="t-ele">2. Enter a Image url</div>
		<div class="t-ele">3. Click the eye to toggle submissions</div>
		<div class="t-ele">4. Click preview to verify that everything works</div>
		<div class="t-ele">
			5. Click the share button, the link goes to your ask page where others can send questions too
		</div>
		<div class="t-inst">Questions:</div>
		<div class="t-ele">6. Use the navigator at the top to see asked questions</div>
		<div class="t-ele">7. You can hide questions from your answered page</div>
		<div class="t-ele">8. You can delete questions</div>
		<div class="t-ele">
			9. You can reply to questions (Type into the reply box and then press enter)
		</div>
	</div>

	<!-- <iframe width="350" height="200" title="intro" class="video" src="https://www.youtube.com/embed/tgbNymZ7vqY"/> -->
	<!-- svelte-ignore a11y-click-events-have-key-events -->
	<div id="start" class="button" on:click={start}>Get Started</div>
</div>

<style>
	.instructions {
		text-align: center;
		margin: 10px;
		overflow-wrap: break-word;
		padding: 2px 2px;
	}

	.t-inst {
		margin: 5px;
		font-size: 20px;
		color: var(--text-dark) !important;
	}

	.t-ele {
		color: var(---text-light) !important;
	}

	.title {
		font-size: 60px;
		color: var(--text-dark);
		margin: 5px;
	}

	.sub-title {
		font-size: 20px;
		color: var(--text-sec);
		margin: 5px;
	}

	/*

	.video {
		margin: 30px;
	}

	*/

	.main {
		flex-direction: column;
		justify-content: center;
		align-items: center;
		display: flex;
	}

	.button {
		padding: 4px 8px;
		border: 1px solid var(--text-sec);
		border-radius: 4px;
		background-color: var(---text-light);
		cursor: pointer;
		color: var(--text-main);
		justify-content: center;
		align-items: center;
		font-size: 25px;
		align-self: center;
	}

	.button:hover {
		border-color: var(--text-dark);
	}

	/*
	@media only screen and (max-width: 600px) {
		iframe {
			height: 300 !important;
			width: 200 !important;
		}
	}
	*/
</style>
