---
search:
  boost: 10.0
---

# Class: Plan 


_Plan associated with using, maintaining, developing, or performing other_

_activities associated with technology_



<div data-search-exclude markdown="1">



URI: [tech:Plan](https://w3id.org/lmodel/dpv/tech/Plan)





```mermaid
 classDiagram
    class Plan
    click Plan href "../Plan/"
      Documentation <|-- Plan
        click Documentation href "../Documentation/"
      

      Plan <|-- DevelopmentPlan
        click DevelopmentPlan href "../DevelopmentPlan/"
      Plan <|-- TestingPlan
        click TestingPlan href "../TestingPlan/"
      

      
```





## Inheritance
* [Documentation](Documentation.md)
    * **Plan**
        * [DevelopmentPlan](DevelopmentPlan.md) [ [Documentation](Documentation.md)]
        * [TestingPlan](TestingPlan.md) [ [Documentation](Documentation.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Plan](https://w3id.org/lmodel/dpv/tech/Plan) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Plan




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#Plan |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Plan |
| native | tech:Plan |
| exact | dpv_tech:Plan, dpv_tech_owl:Plan |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Plan
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Plan
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'Plan associated with using, maintaining, developing, or performing other

  activities associated with technology'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Plan
exact_mappings:
- dpv_tech:Plan
- dpv_tech_owl:Plan
is_a: Documentation
class_uri: tech:Plan

```
</details>

### Induced

<details>
```yaml
name: Plan
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Plan
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'Plan associated with using, maintaining, developing, or performing other

  activities associated with technology'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Plan
exact_mappings:
- dpv_tech:Plan
- dpv_tech_owl:Plan
is_a: Documentation
class_uri: tech:Plan

```
</details></div>