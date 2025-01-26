<script lang="ts">
    import { page } from "$app/state";

    let name = page.params["username"];
</script>

Welcome: {name}
