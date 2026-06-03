---
search:
  boost: 10.0
---

# Class: NotProvided 


_Status indicating Technology has not been provided_



<div data-search-exclude markdown="1">



URI: [tech:NotProvided](https://w3id.org/lmodel/dpv/tech/NotProvided)





```mermaid
 classDiagram
    class NotProvided
    click NotProvided href "../NotProvided/"
      ProvisionStatus <|-- NotProvided
        click ProvisionStatus href "../ProvisionStatus/"
      
      
```





## Inheritance
* [TechnologyStatus](TechnologyStatus.md)
    * [ProvisionStatus](ProvisionStatus.md)
        * **NotProvided**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:NotProvided](https://w3id.org/lmodel/dpv/tech/NotProvided) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Not Provided




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#NotProvided |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:NotProvided |
| native | tech:NotProvided |
| exact | dpv_tech:NotProvided, dpv_tech_owl:NotProvided |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NotProvided
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#NotProvided
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Status indicating Technology has not been provided
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Not Provided
exact_mappings:
- dpv_tech:NotProvided
- dpv_tech_owl:NotProvided
is_a: ProvisionStatus
class_uri: tech:NotProvided

```
</details>

### Induced

<details>
```yaml
name: NotProvided
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#NotProvided
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Status indicating Technology has not been provided
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Not Provided
exact_mappings:
- dpv_tech:NotProvided
- dpv_tech_owl:NotProvided
is_a: ProvisionStatus
class_uri: tech:NotProvided

```
</details></div>