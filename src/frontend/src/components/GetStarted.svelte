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
	<iframe
		width="350"
		height="200"
		title="intro"
		class="video"
		src="https://www.youtube.com/embed/tgbNymZ7vqY"
	/>
	<!-- svelte-ignore a11y-click-events-have-key-events -->
	<div id="start" class="button" on:click={start}>Get Started</div>
</div>

<style>
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

	.video {
		margin: 30px;
	}

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

	@media only screen and (max-width: 600px) {
		iframe {
			height: 300 !important;
			width: 200 !important;
		}
	}
</style>
