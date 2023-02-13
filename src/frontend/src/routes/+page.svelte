<script>
	import { onMount } from 'svelte';
	import GetStarted from '../components/GetStarted.svelte';

	let datac = [];
	let checkNewUser;
	onMount(async () => {
		try {
			const data = await fetch('/api/config');
			datac = await data.json();
			checkNewUser = datac['user_state']['value'];
		} catch {
			fetch(`/api/config`, {
				method: 'POST',
				headers: {
					'Content-type': 'application/json'
				},
				body: JSON.stringify({ value: true, key: 'user_state' })
			}).then(window.location.reload);
		}

		if (checkNewUser === false) {
			window.location.href = `/dashboard`;
		} else if (checkNewUser === null) {
			fetch(`/api/config`, {
				method: 'POST',
				headers: {
					'Content-type': 'application/json'
				},
				body: JSON.stringify({ value: true, key: 'user_state' })
			}).then(window.location.reload);
		}
	});
</script>

{#if checkNewUser}
	<GetStarted />
{/if}
