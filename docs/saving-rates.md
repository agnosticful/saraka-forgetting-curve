# Calculating saving rate

## Ver 1: Original formula

![](https://user-images.githubusercontent.com/4289883/54080652-95b3b700-42a9-11e9-9aac-03c2b1777270.png)

```js
const calculateSavingRate = elapsedMinutes =>
  elapsedMinutes === 0
    ? 1
    : 1.84 / (Math.pow(Math.log10(elapsedMinutes), 1.25) + 1.84);
```

## Ver 2: Enhanced formula

![](https://user-images.githubusercontent.com/4289883/54080659-afed9500-42a9-11e9-832f-dce3a7e9d984.png)

```js
const calculateSavingRate2 = elapsedMinutes =>
  elapsedMinutes === 0
    ? 1
    : 15.297 /
      Math.pow(Math.log10(elapsedMinutes / (1.224 * Math.pow(10, -4))), 2);
```
