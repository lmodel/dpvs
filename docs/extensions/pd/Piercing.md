---
search:
  boost: 10.0
---

# Class: Piercing 


_Information about piercings_



<div data-search-exclude markdown="1">



URI: [pd:Piercing](https://w3id.org/lmodel/dpv/pd/Piercing)





```mermaid
 classDiagram
    class Piercing
    click Piercing href "../Piercing/"
      PhysicalCharacteristic <|-- Piercing
        click PhysicalCharacteristic href "../PhysicalCharacteristic/"
      
      
```





## Inheritance
* [External](External.md)
    * [PhysicalCharacteristic](PhysicalCharacteristic.md)
        * **Piercing**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Piercing](https://w3id.org/lmodel/dpv/pd/Piercing) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Piercing




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Piercing |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Piercing |
| native | pd:Piercing |
| exact | dpv_pd:Piercing, dpv_pd_owl:Piercing |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Piercing
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Piercing
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about piercings
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Piercing
exact_mappings:
- dpv_pd:Piercing
- dpv_pd_owl:Piercing
is_a: PhysicalCharacteristic
class_uri: pd:Piercing

```
</details>

### Induced

<details>
```yaml
name: Piercing
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Piercing
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about piercings
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Piercing
exact_mappings:
- dpv_pd:Piercing
- dpv_pd_owl:Piercing
is_a: PhysicalCharacteristic
class_uri: pd:Piercing

```
</details></div>