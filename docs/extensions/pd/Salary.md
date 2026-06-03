---
search:
  boost: 10.0
---

# Class: Salary 


_Information about salary_



<div data-search-exclude markdown="1">



URI: [pd:Salary](https://w3id.org/lmodel/dpv/pd/Salary)





```mermaid
 classDiagram
    class Salary
    click Salary href "../Salary/"
      Professional <|-- Salary
        click Professional href "../Professional/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [Professional](Professional.md)
        * **Salary**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Salary](https://w3id.org/lmodel/dpv/pd/Salary) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Salary




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Salary |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Salary |
| native | pd:Salary |
| exact | dpv_pd:Salary, dpv_pd_owl:Salary |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Salary
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Salary
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about salary
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Salary
exact_mappings:
- dpv_pd:Salary
- dpv_pd_owl:Salary
is_a: Professional
class_uri: pd:Salary

```
</details>

### Induced

<details>
```yaml
name: Salary
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Salary
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about salary
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Salary
exact_mappings:
- dpv_pd:Salary
- dpv_pd_owl:Salary
is_a: Professional
class_uri: pd:Salary

```
</details></div>