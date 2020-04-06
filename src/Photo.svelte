<script>
  export let booster;

  let width = 300;
  let height = 200;

  let url = booster.asset + '?w=' + width + '&h=' + height + '&fit=crop&crop=faces';
</script>

<div class="card {booster.type}">
  <img src="{url}" alt="Smile Minnesota photo"/>
  <p>{booster.story}</p>
</div>
