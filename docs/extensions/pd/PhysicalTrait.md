---
search:
  boost: 10.0
---

# Class: PhysicalTrait 


_Information about defining traits or features regarding the body_



<div data-search-exclude markdown="1">



URI: [pd:PhysicalTrait](https://w3id.org/lmodel/dpv/pd/PhysicalTrait)





```mermaid
 classDiagram
    class PhysicalTrait
    click PhysicalTrait href "../PhysicalTrait/"
      Demographic <|-- PhysicalTrait
        click Demographic href "../Demographic/"
      
      
```





## Inheritance
* [External](External.md)
    * [Demographic](Demographic.md)
        * **PhysicalTrait**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:PhysicalTrait](https://w3id.org/lmodel/dpv/pd/PhysicalTrait) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Physical Trait




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#PhysicalTrait |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:PhysicalTrait |
| native | pd:PhysicalTrait |
| exact | dpv_pd:PhysicalTrait, dpv_pd_owl:PhysicalTrait |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PhysicalTrait
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PhysicalTrait
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about defining traits or features regarding the body
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Physical Trait
exact_mappings:
- dpv_pd:PhysicalTrait
- dpv_pd_owl:PhysicalTrait
is_a: Demographic
class_uri: pd:PhysicalTrait

```
</details>

### Induced

<details>
```yaml
name: PhysicalTrait
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PhysicalTrait
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about defining traits or features regarding the body
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Physical Trait
exact_mappings:
- dpv_pd:PhysicalTrait
- dpv_pd_owl:PhysicalTrait
is_a: Demographic
class_uri: pd:PhysicalTrait

```
</details></div>