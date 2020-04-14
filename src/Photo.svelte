<script>
  export let booster;

  let pWidth = 400;
  let pHeight = 400;

  let lWidth = 600;
  let lHeight = 350;

  let pUrl = booster.asset + '?w=' + pWidth + '&h=' + pHeight + '&fit=crop&crop=faces';
  let lUrl = booster.asset + '?w=' + lWidth + '&h=' + lHeight + '&fit=crop&crop=faces';
</script>

{#if booster.from_strib === "TRUE"}

  {#if booster.shape === "Portrait"}

    <div class="card strib {booster.type} portrait">
      <img src="{pUrl}" alt="Smile Minnesota photo"/>
      <div class="text">
        <h5 class="stamp">{booster.timestamp}</h5>
        <p>{booster.story}</p>
        <h4 class="author">— {booster.name}</h4>
      </div>
    </div>

  {:else}

    <div class="card strib {booster.type} landscape">
      <img src="{lUrl}" alt="Smile Minnesota photo"/>
      <div class="text">
        <h5 class="stamp">{booster.timestamp}</h5>
        <p>{booster.story}</p>
        <h4 class="author">— {booster.name}</h4>
      </div>
    </div>

  {/if}



{:else}

  {#if booster.shape === "Portrait"}

    <div class="card {booster.type} portrait">
      <img src="{pUrl}" alt="Smile Minnesota photo"/>
      <div class="text">
        <h5 class="stamp">{booster.timestamp}</h5>
        <p>{booster.story}</p>
        <h4 class="author">— {booster.name}</h4>
      </div>
    </div>

  {:else}

    <div class="card {booster.type} landscape">
      <img src="{lUrl}" alt="Smile Minnesota photo"/>
      <div class="text">
        <h5 class="stamp">{booster.timestamp}</h5>
        <p>{booster.story}</p>
        <h4 class="author">— {booster.name}</h4>
      </div>
    </div>

  {/if}

{/if}
