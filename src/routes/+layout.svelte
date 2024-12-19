<script lang="ts">
	import Navbar from '@componets/navbar.svelte';
	import Footer from '@componets/footer.svelte';
	import '../app.css';

	let { children } = $props();
</script>

<div class="flex h-screen flex-col">
	<Navbar />

	<main class="flex-grow">
		{@render children()}
	</main>

	<Footer />
</div>
