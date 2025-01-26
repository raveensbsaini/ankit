<script lang="ts">
    import { dev } from "$app/environment";

    /// ------------------- in constants.ts
    let url = "";
    if (dev) {
        url = "http://localhost:8000";
    }
    /// ------------------------

    let count = $state(null);

    async function load_data() {
        let response = await fetch(url + "/data"); // <--- production
        count = (await response.json())["count"];
    }
</script>

<div class="p-5">
    <button class="p-2 rounded border" onclick={load_data}> Load</button>

    {#if count !== null}
        <h1>Count: {count}</h1>
    {/if}
</div>
