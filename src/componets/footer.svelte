<script>
	import { Github } from 'lucide-svelte';
	import { PenTool } from 'lucide-svelte';
</script>

<footer class="footer items-center bg-neutral p-4 text-neutral-content">
	<aside class="grid-flow-col items-center">
		<PenTool />
		<p>Copyright {new Date().getFullYear()} Wilaz - Licensed under AGPL-3.0 or later.</p>
	</aside>
	<nav class="grid-flow-col gap-4 md:place-self-center md:justify-self-end">
		<a href="https://github.com/Wilaz">
			<Github />
		</a>
	</nav>
</footer>
