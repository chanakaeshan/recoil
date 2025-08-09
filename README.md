# Recoil

Welcome to the **Recoil** repository! This project is maintained by [@chanakaeshan](https://github.com/chanakaeshan).

## Overview

_Recoil_ is a project designed to provide state management solutions for modern JavaScript applications. It offers an intuitive and flexible API for managing global and local state, making it easier to build scalable and maintainable apps.

## Features

- **Simple State Management:** Easily manage both global and local state without prop drilling.
- **Performance:** Optimized for fast updates and minimal re-renders.
- **Flexible API:** Supports atoms, selectors, and other advanced patterns.
- **Developer Friendly:** Designed for ease-of-use and productivity.

## Installation

```bash
npm install @chanakaeshan/recoil
```

or

```bash
yarn add @chanakaeshan/recoil
```

## Usage

```js
import { atom, selector, useRecoilState, useRecoilValue } from '@chanakaeshan/recoil';

// Define an atom
const countState = atom({
  key: 'countState',
  default: 0,
});

// Using Recoil state in a component
function Counter() {
  const [count, setCount] = useRecoilState(countState);
  return (
    <div>
      <button onClick={() => setCount(count - 1)}>-</button>
      <span>{count}</span>
      <button onClick={() => setCount(count + 1)}>+</button>
    </div>
  );
}
```

## Documentation

For detailed documentation, usage examples, and API references, please refer to the [official documentation](https://github.com/chanakaeshan/recoil/wiki).

## Contributing

Contributions are welcome! Please open issues or pull requests to help improve the project.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for more information.

## License

This project is licensed under the [MIT License](LICENSE).

---

**Happy coding!**
