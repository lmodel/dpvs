---
search:
  boost: 10.0
---

# Class: TestingPlan 


_Plan associated with testing technology_



<div data-search-exclude markdown="1">



URI: [tech:TestingPlan](https://w3id.org/lmodel/dpv/tech/TestingPlan)





```mermaid
 classDiagram
    class TestingPlan
    click TestingPlan href "../TestingPlan/"
      Documentation <|-- TestingPlan
        click Documentation href "../Documentation/"
      Plan <|-- TestingPlan
        click Plan href "../Plan/"
      
      
```





## Inheritance
* [Documentation](Documentation.md)
    * [Plan](Plan.md)
        * **TestingPlan** [ [Documentation](Documentation.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:TestingPlan](https://w3id.org/lmodel/dpv/tech/TestingPlan) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Testing Plan




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#TestingPlan |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:TestingPlan |
| native | tech:TestingPlan |
| exact | dpv_tech:TestingPlan, dpv_tech_owl:TestingPlan |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TestingPlan
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#TestingPlan
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Plan associated with testing technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Testing Plan
exact_mappings:
- dpv_tech:TestingPlan
- dpv_tech_owl:TestingPlan
is_a: Plan
mixins:
- Documentation
class_uri: tech:TestingPlan

```
</details>

### Induced

<details>
```yaml
name: TestingPlan
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#TestingPlan
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Plan associated with testing technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Testing Plan
exact_mappings:
- dpv_tech:TestingPlan
- dpv_tech_owl:TestingPlan
is_a: Plan
mixins:
- Documentation
class_uri: tech:TestingPlan

```
</details></div>