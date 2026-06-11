When expressed in mathematical terms, the relations are equations and the rates are derivatives. **Equations** containing **derivatives** are **differential equations**. 
An equation that describe a physical process is called **Mathematical Model**

A differential equation is an equation that relates a function with its own derivatives. Instead of solving for a number, you're solving for a **_function_**. For example:
$$
dy/dx = 2x
$$
This says "find a function y whose derivative is $2x$." The answer is $y = x² + C.$

---
# Methods to solve

- **Separation of variables:** [[Separation of Variables]]

**Quick rule of thumb:** Try separation first. If you end up with y² or something that can't be separated cleanly, check if the equation is linear — then reach for the integrating factor.

|                   | Separation of Variables              | Integrating Factor                                 |
| ----------------- | ------------------------------------ | -------------------------------------------------- |
| **Equation form** | dy/dx = f(x) · g(y)                  | dy/dx + P(x)·y = Q(x)                              |
| **Key operation** | Split and integrate each side        | Multiply by a clever factor μ(x)                   |
| **When to use**   | When you can isolate y and x cleanly | When the equation is linear in y but not separable |
| **Result**        | Often exponential or implicit        | Always explicit formula for y                      |
