---
search:
  boost: 10.0
---

# Class: Emotion 


_Information about emotion_



<div data-search-exclude markdown="1">



URI: [pd:Emotion](https://w3id.org/lmodel/dpv/pd/Emotion)





```mermaid
 classDiagram
    class Emotion
    click Emotion href "../Emotion/"
      Internal <|-- Emotion
        click Internal href "../Internal/"
      
      
```





## Inheritance
* [Internal](Internal.md)
    * **Emotion**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Emotion](https://w3id.org/lmodel/dpv/pd/Emotion) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Emotion




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Emotion |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Emotion |
| native | pd:Emotion |
| exact | dpv_pd:Emotion, dpv_pd_owl:Emotion |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Emotion
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Emotion
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about emotion
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Emotion
exact_mappings:
- dpv_pd:Emotion
- dpv_pd_owl:Emotion
is_a: Internal
class_uri: pd:Emotion

```
</details>

### Induced

<details>
```yaml
name: Emotion
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Emotion
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about emotion
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Emotion
exact_mappings:
- dpv_pd:Emotion
- dpv_pd_owl:Emotion
is_a: Internal
class_uri: pd:Emotion

```
</details></div>