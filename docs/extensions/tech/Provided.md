---
search:
  boost: 10.0
---

# Class: Provided 


_Status indicating Technology has been provided_



<div data-search-exclude markdown="1">



URI: [tech:Provided](https://w3id.org/lmodel/dpv/tech/Provided)





```mermaid
 classDiagram
    class Provided
    click Provided href "../Provided/"
      ProvisionStatus <|-- Provided
        click ProvisionStatus href "../ProvisionStatus/"
      
      
```





## Inheritance
* [TechnologyStatus](TechnologyStatus.md)
    * [ProvisionStatus](ProvisionStatus.md)
        * **Provided**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Provided](https://w3id.org/lmodel/dpv/tech/Provided) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Provided




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#Provided |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Provided |
| native | tech:Provided |
| exact | dpv_tech:Provided, dpv_tech_owl:Provided |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Provided
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Provided
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Status indicating Technology has been provided
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided
exact_mappings:
- dpv_tech:Provided
- dpv_tech_owl:Provided
is_a: ProvisionStatus
class_uri: tech:Provided

```
</details>

### Induced

<details>
```yaml
name: Provided
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Provided
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Status indicating Technology has been provided
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided
exact_mappings:
- dpv_tech:Provided
- dpv_tech_owl:Provided
is_a: ProvisionStatus
class_uri: tech:Provided

```
</details></div>