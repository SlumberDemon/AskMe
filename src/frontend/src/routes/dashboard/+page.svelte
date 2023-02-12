<script>
	import { onMount } from 'svelte';

	let mainData = [];
	let displayName = '';
	let displayImg = '';
	let subState = '';

	onMount(async () => {
		document.getElementById('dash').style.backgroundColor = 'var(--highlight-main)';

		const data = await fetch('/api/config');
		mainData = await data.json();

		try {
			displayName = mainData['display_name']['value'];
			displayImg = mainData['display_image']['value'];
			subState = mainData['submissions_state']['value'];
		} catch {}

		const shareBtn = document.getElementById('share');
		const saveImg = document.getElementById('save-image');
		const saveNam = document.getElementById('save-name');
		const previewBtn = document.getElementById('preview');
		const subBtn = document.getElementById('submissions');

		subBtn.addEventListener('click', () => {
			if (subState === true) {
				fetch(`/api/config`, {
					method: 'POST',
					headers: {
						'Content-type': 'application/json'
					},
					body: JSON.stringify({ value: false, key: 'submissions_state' })
				}).then(() => {
					window.location.reload();
				});
			} else {
				fetch(`/api/config`, {
					method: 'POST',
					headers: {
						'Content-type': 'application/json'
					},
					body: JSON.stringify({ value: true, key: 'submissions_state' })
				}).then(() => {
					window.location.reload();
				});
			}
		});

		previewBtn.addEventListener('click', () => {
			window.open(`${window.location.origin}/preview`);
		});

		shareBtn.addEventListener('click', () => {
			let url = `${window.location.origin}/ask`;
			navigator.clipboard.writeText(url).then(() => {
				alert('Copied url to clipboard');
			});
			// shareBtn.style.borderColor = `var(--confirm)`;
			//setTimeout(() => {
			// shareBtn.style.borderColor = `var(--highlight-main)`;
			// }, 800);
		});

		saveNam.addEventListener('click', () => {
			const name = document.getElementById('name');
			if (name.value === '') {
				name.placeholder = `Please enter a name`;
				setTimeout(() => {
					name.placeholder = `Display name`;
				}, 800);
				return;
			}
			fetch(`/api/config`, {
				method: 'POST',
				headers: {
					'Content-type': 'application/json'
				},
				body: JSON.stringify({ value: name.value, key: 'display_name' })
			}).then(() => {
				setTimeout(() => {
					shareBtn.style.borderColor = `var(--highlight-main)`;
				}, 800);
			});
		});

		saveImg.addEventListener('click', () => {
			const url = document.getElementById('url');
			if (url.value === '') {
				url.placeholder = `Please enter a url`;
				setTimeout(() => {
					url.placeholder = `Display image url`;
				}, 800);
				return;
			}
			fetch(`/api/config`, {
				method: 'POST',
				headers: {
					'Content-type': 'application/json'
				},
				body: JSON.stringify({ value: url.value, key: 'display_image' })
			}).then(() => {
				saveImg.style.borderColor = `var(--confirm)`;
				setTimeout(() => {
					saveImg.style.borderColor = `var(--highlight-main)`;
				}, 800);
			});
		});
	});
</script>

<nav>
	<div class="nav-items">
		<div class="nav-ele" id="dash"><a href="/dashboard">Dashboard</a></div>
		<div class="nav-sep">/</div>
		<div class="nav-ele" id="ques"><a href="/questions">Questions</a></div>
	</div>
</nav>

<div class="dashboard">
	<div class="page-name">Dashboard</div>
	<div class="page-content">
		<div class="control-panel">
			<div class="control-ele">
				<div class="button" id="save-name">
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
						class="feather feather-save"
						><path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z" /><polyline
							points="17 21 17 13 7 13 7 21"
						/><polyline points="7 3 7 8 15 8" /></svg
					>
				</div>
				<input type="text" id="name" class="input" placeholder="Display name" value={displayName} />
			</div>
			<div class="control-ele">
				<div class="button" id="save-image">
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
						class="feather feather-save"
						><path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z" /><polyline
							points="17 21 17 13 7 13 7 21"
						/><polyline points="7 3 7 8 15 8" /></svg
					>
				</div>
				<input
					type="url"
					id="url"
					class="input"
					placeholder="Display image url"
					value={displayImg}
				/>
			</div>
			<div class="control-ele">
				<div class="button" id="submissions">
					{#if subState}
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
				<div class="dsc-text">Toggle Submissions</div>
			</div>
			<div class="control-ele">
				<div class="button" id="share">
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
						class="feather feather-share"
						><path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8" /><polyline
							points="16 6 12 2 8 6"
						/><line x1="12" y1="2" x2="12" y2="15" /></svg
					>
				</div>
				<div class="dsc-text">Share</div>
			</div>
			<div class="control-ele">
				<div id="preview" class="button">Preview</div>
			</div>
		</div>
	</div>
</div>

<style>
	.page-name {
		font-size: 25px;
		margin: 5px;
	}

	.page-content {
		margin: 10px;
	}

	.dashboard {
		margin: 10px;
		display: flex;
		align-items: center;
		justify-content: center;
		flex-direction: column;
	}

	.control-ele {
		display: flex;
		flex-direction: row;
		gap: 8px;
		align-items: center;
		margin: 10px;
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

	.dsc-text {
		font-size: 15px;
	}

	.input {
		padding: 6px 20px;
		border-radius: 4px;
		text-align: left;
		border: 1px solid var(--highlight-main);
		background-color: var(--highlight-sec);
		width: 150px;
	}

	.input:focus {
		border-color: var(--text-sec);
		color: var(--text-main);
		outline: none;
	}
</style>
