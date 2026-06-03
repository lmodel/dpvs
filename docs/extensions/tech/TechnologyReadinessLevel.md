---
search:
  boost: 10.0
---

# Class: TechnologyReadinessLevel 


_Indication of maturity of Technology (ISO 16290:2013)_



<div data-search-exclude markdown="1">



URI: [tech:TechnologyReadinessLevel](https://w3id.org/lmodel/dpv/tech/TechnologyReadinessLevel)





```mermaid
 classDiagram
    class TechnologyReadinessLevel
    click TechnologyReadinessLevel href "../TechnologyReadinessLevel/"
      TechnologyStatus <|-- TechnologyReadinessLevel
        click TechnologyStatus href "../TechnologyStatus/"
      
      
```





## Inheritance
* [TechnologyStatus](TechnologyStatus.md)
    * **TechnologyReadinessLevel**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:TechnologyReadinessLevel](https://w3id.org/lmodel/dpv/tech/TechnologyReadinessLevel) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Technology Readiness Level (TRL)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#TechnologyReadinessLevel |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:TechnologyReadinessLevel |
| native | tech:TechnologyReadinessLevel |
| exact | dpv_tech:TechnologyReadinessLevel, dpv_tech_owl:TechnologyReadinessLevel |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TechnologyReadinessLevel
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#TechnologyReadinessLevel
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indication of maturity of Technology (ISO 16290:2013)
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Technology Readiness Level (TRL)
exact_mappings:
- dpv_tech:TechnologyReadinessLevel
- dpv_tech_owl:TechnologyReadinessLevel
is_a: TechnologyStatus
class_uri: tech:TechnologyReadinessLevel

```
</details>

### Induced

<details>
```yaml
name: TechnologyReadinessLevel
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#TechnologyReadinessLevel
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indication of maturity of Technology (ISO 16290:2013)
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Technology Readiness Level (TRL)
exact_mappings:
- dpv_tech:TechnologyReadinessLevel
- dpv_tech_owl:TechnologyReadinessLevel
is_a: TechnologyStatus
class_uri: tech:TechnologyReadinessLevel

```
</details></div>