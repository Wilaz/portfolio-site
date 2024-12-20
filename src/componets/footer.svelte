<script lang="ts">
	import Git from '@componets/git.svelte';
</script>

<footer class="footer items-center bg-neutral p-4 text-neutral-content">
	<aside class="grid-flow-col items-center">
		<p>Copyright {new Date().getFullYear()} Wilaz - Licensed under AGPL-3.0 or later.</p>
	</aside>
	<nav class="grid-flow-col gap-4 md:place-self-center md:justify-self-end">
		<a href="https://github.com/Wilaz" aria-label="git">
			<Git />
		</a>
	</nav>
</footer>
