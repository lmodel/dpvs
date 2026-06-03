---
search:
  boost: 10.0
---

# Class: SkinTone 


_Information about skin tone_



<div data-search-exclude markdown="1">



URI: [pd:SkinTone](https://w3id.org/lmodel/dpv/pd/SkinTone)





```mermaid
 classDiagram
    class SkinTone
    click SkinTone href "../SkinTone/"
      PhysicalCharacteristic <|-- SkinTone
        click PhysicalCharacteristic href "../PhysicalCharacteristic/"
      
      
```





## Inheritance
* [External](External.md)
    * [PhysicalCharacteristic](PhysicalCharacteristic.md)
        * **SkinTone**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:SkinTone](https://w3id.org/lmodel/dpv/pd/SkinTone) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Skin Tone




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#SkinTone |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:SkinTone |
| native | pd:SkinTone |
| exact | dpv_pd:SkinTone, dpv_pd_owl:SkinTone |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SkinTone
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#SkinTone
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about skin tone
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Skin Tone
exact_mappings:
- dpv_pd:SkinTone
- dpv_pd_owl:SkinTone
is_a: PhysicalCharacteristic
class_uri: pd:SkinTone

```
</details>

### Induced

<details>
```yaml
name: SkinTone
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#SkinTone
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about skin tone
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Skin Tone
exact_mappings:
- dpv_pd:SkinTone
- dpv_pd_owl:SkinTone
is_a: PhysicalCharacteristic
class_uri: pd:SkinTone

```
</details></div>