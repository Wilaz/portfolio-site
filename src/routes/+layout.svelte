<script lang="ts">
	import Navbar from '@componets/navbar.svelte';
	import Footer from '@componets/footer.svelte';
	import '../app.css';
	let { children } = $props();
</script>

<div class="flex flex-col h-screen">

<Navbar />

<div class="flex-grow">
	{@render children()}
</div>

<Footer />

</div>