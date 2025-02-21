<script>
  function on_submit(){
    console.log("This is another function")
  }
</script>
<form on:submit = { on_submit }>
  <h1>Please select time</h1>
  <select>
    <option>1</option>
    <option>2</option>
    <option>3</option>
    <option>4</option>
    <option>5</option>
    <option>6</option>
    <option>7</option>
    <option>8</option>
    <option>9</option>
    <option>10</option>
    <option>11</option>
    <option>12</option>
  </select>
  <select>
    <option>am</option>
    <option>pm</option>
  </select>
  <input type="submit">
</form>
