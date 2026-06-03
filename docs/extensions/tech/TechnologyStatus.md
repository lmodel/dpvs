---
search:
  boost: 10.0
---

# Class: TechnologyStatus 


_Status associated with development, deployment, and use of technology_



<div data-search-exclude markdown="1">



URI: [tech:TechnologyStatus](https://w3id.org/lmodel/dpv/tech/TechnologyStatus)





```mermaid
 classDiagram
    class TechnologyStatus
    click TechnologyStatus href "../TechnologyStatus/"
      TechnologyStatus <|-- MarketAvailabilityStatus
        click MarketAvailabilityStatus href "../MarketAvailabilityStatus/"
      TechnologyStatus <|-- ProvisionStatus
        click ProvisionStatus href "../ProvisionStatus/"
      TechnologyStatus <|-- TechnologyReadinessLevel
        click TechnologyReadinessLevel href "../TechnologyReadinessLevel/"
      
      
```





## Inheritance
* **TechnologyStatus**
    * [MarketAvailabilityStatus](MarketAvailabilityStatus.md)
    * [ProvisionStatus](ProvisionStatus.md)
    * [TechnologyReadinessLevel](TechnologyReadinessLevel.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:TechnologyStatus](https://w3id.org/lmodel/dpv/tech/TechnologyStatus) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Technology Status




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#TechnologyStatus |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:TechnologyStatus |
| native | tech:TechnologyStatus |
| exact | dpv_tech:TechnologyStatus, dpv_tech_owl:TechnologyStatus |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TechnologyStatus
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#TechnologyStatus
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Status associated with development, deployment, and use of technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Technology Status
exact_mappings:
- dpv_tech:TechnologyStatus
- dpv_tech_owl:TechnologyStatus
class_uri: tech:TechnologyStatus

```
</details>

### Induced

<details>
```yaml
name: TechnologyStatus
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#TechnologyStatus
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Status associated with development, deployment, and use of technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Technology Status
exact_mappings:
- dpv_tech:TechnologyStatus
- dpv_tech_owl:TechnologyStatus
class_uri: tech:TechnologyStatus

```
</details></div>