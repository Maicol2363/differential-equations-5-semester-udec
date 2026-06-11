This method works when you can algebraically separate all the y's to one side and all the x's to the other. Then you integrate both sides independently.
The key idea: if the equation looks like $dy/dx = f(x) · g(y)$, you can rewrite it as:
$$dy / g(y) = f(x) dx
$$
 → then integrate both sides
# The Analytical Engine: 6-Step Methodology

### 1. Format
Write as $\dfrac{dy}{dx} = f(x, y)$
### 2. Diagnose
Verificar factorizabilidad $(f(x) \cdot g(y))$
### 3. Separate
Aislar variables: $$\left[\frac{dy}{g(y)}\right] = \left[f(x),dx\right]$$
### 4. Integrate
Aplicar $\int$ a ambos lados de la frontera analítica
### 5. Solve
Resolver integrales y aislar $y$ → **Solución General**
### 6. Anchor
Aplicar condición inicial para hallar $C$ → **Solución Particular**

---
**Separable ODE**
$\frac{dy}{dx} = h_1(x),h_2(y)$
- **$h_1(x)$** → function of **$x$** only  
- **$h_2(y)$** → function of **$y$** only

**Separation**
$\frac{1}{h_2(y)},dy = h_1(x),dx$

**Define**
- **$m(x) = h_1(x)$**
- **$n(y) = \frac{1}{h_2(y)}$**
**Result**
$n(y),dy = m(x),dx$
**Equivalent differential form**
$m(x),dx - n(y),dy = 0$

# Problems
![[Xpp_SeparationOfVariables.pdf]]
[[Partial Fraction Descomposion]] -> Remember it to solve a problem inside the last pdf

### D.E Singular Problem
![[Xpp_SeparationVariables_singularSolution.pdf]]
---
![[20260317_110413.jpg]]