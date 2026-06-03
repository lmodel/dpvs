---
search:
  boost: 10.0
---

# Class: DevelopmentPlan 


_Plan associated with developing technology_



<div data-search-exclude markdown="1">



URI: [tech:DevelopmentPlan](https://w3id.org/lmodel/dpv/tech/DevelopmentPlan)





```mermaid
 classDiagram
    class DevelopmentPlan
    click DevelopmentPlan href "../DevelopmentPlan/"
      Documentation <|-- DevelopmentPlan
        click Documentation href "../Documentation/"
      Plan <|-- DevelopmentPlan
        click Plan href "../Plan/"
      
      
```





## Inheritance
* [Documentation](Documentation.md)
    * [Plan](Plan.md)
        * **DevelopmentPlan** [ [Documentation](Documentation.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:DevelopmentPlan](https://w3id.org/lmodel/dpv/tech/DevelopmentPlan) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Development Plan




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#DevelopmentPlan |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:DevelopmentPlan |
| native | tech:DevelopmentPlan |
| exact | dpv_tech:DevelopmentPlan, dpv_tech_owl:DevelopmentPlan |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DevelopmentPlan
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#DevelopmentPlan
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Plan associated with developing technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Development Plan
exact_mappings:
- dpv_tech:DevelopmentPlan
- dpv_tech_owl:DevelopmentPlan
is_a: Plan
mixins:
- Documentation
class_uri: tech:DevelopmentPlan

```
</details>

### Induced

<details>
```yaml
name: DevelopmentPlan
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#DevelopmentPlan
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Plan associated with developing technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Development Plan
exact_mappings:
- dpv_tech:DevelopmentPlan
- dpv_tech_owl:DevelopmentPlan
is_a: Plan
mixins:
- Documentation
class_uri: tech:DevelopmentPlan

```
</details></div>