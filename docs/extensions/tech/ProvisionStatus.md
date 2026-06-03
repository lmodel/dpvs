---
search:
  boost: 10.0
---

# Class: ProvisionStatus 


_Status indicating whether Technology has been provided_



<div data-search-exclude markdown="1">



URI: [tech:ProvisionStatus](https://w3id.org/lmodel/dpv/tech/ProvisionStatus)





```mermaid
 classDiagram
    class ProvisionStatus
    click ProvisionStatus href "../ProvisionStatus/"
      TechnologyStatus <|-- ProvisionStatus
        click TechnologyStatus href "../TechnologyStatus/"
      

      ProvisionStatus <|-- NotProvided
        click NotProvided href "../NotProvided/"
      ProvisionStatus <|-- Provided
        click Provided href "../Provided/"
      

      
```





## Inheritance
* [TechnologyStatus](TechnologyStatus.md)
    * **ProvisionStatus**
        * [NotProvided](NotProvided.md)
        * [Provided](Provided.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:ProvisionStatus](https://w3id.org/lmodel/dpv/tech/ProvisionStatus) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Provision Status




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#ProvisionStatus |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:ProvisionStatus |
| native | tech:ProvisionStatus |
| exact | dpv_tech:ProvisionStatus, dpv_tech_owl:ProvisionStatus |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProvisionStatus
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvisionStatus
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Status indicating whether Technology has been provided
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provision Status
exact_mappings:
- dpv_tech:ProvisionStatus
- dpv_tech_owl:ProvisionStatus
is_a: TechnologyStatus
class_uri: tech:ProvisionStatus

```
</details>

### Induced

<details>
```yaml
name: ProvisionStatus
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvisionStatus
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Status indicating whether Technology has been provided
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provision Status
exact_mappings:
- dpv_tech:ProvisionStatus
- dpv_tech_owl:ProvisionStatus
is_a: TechnologyStatus
class_uri: tech:ProvisionStatus

```
</details></div>