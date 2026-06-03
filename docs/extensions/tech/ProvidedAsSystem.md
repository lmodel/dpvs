---
search:
  boost: 10.0
---

# Class: ProvidedAsSystem 


_Technology provided as a system_



<div data-search-exclude markdown="1">



URI: [tech:ProvidedAsSystem](https://w3id.org/lmodel/dpv/tech/ProvidedAsSystem)





```mermaid
 classDiagram
    class ProvidedAsSystem
    click ProvidedAsSystem href "../ProvidedAsSystem/"
      ProvisionMethod <|-- ProvidedAsSystem
        click ProvisionMethod href "../ProvisionMethod/"
      
      
```





## Inheritance
* [ProvisionMethod](ProvisionMethod.md)
    * **ProvidedAsSystem**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:ProvidedAsSystem](https://w3id.org/lmodel/dpv/tech/ProvidedAsSystem) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Provided as SystemProvision




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#ProvidedAsSystem |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:ProvidedAsSystem |
| native | tech:ProvidedAsSystem |
| exact | dpv_tech:ProvidedAsSystem, dpv_tech_owl:ProvidedAsSystem |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProvidedAsSystem
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvidedAsSystem
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology provided as a system
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided as SystemProvision
exact_mappings:
- dpv_tech:ProvidedAsSystem
- dpv_tech_owl:ProvidedAsSystem
is_a: ProvisionMethod
class_uri: tech:ProvidedAsSystem

```
</details>

### Induced

<details>
```yaml
name: ProvidedAsSystem
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvidedAsSystem
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology provided as a system
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided as SystemProvision
exact_mappings:
- dpv_tech:ProvidedAsSystem
- dpv_tech_owl:ProvidedAsSystem
is_a: ProvisionMethod
class_uri: tech:ProvidedAsSystem

```
</details></div>