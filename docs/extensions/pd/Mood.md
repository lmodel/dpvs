---
search:
  boost: 10.0
---

# Class: Mood 


_Information about mood_



<div data-search-exclude markdown="1">



URI: [pd:Mood](https://w3id.org/lmodel/dpv/pd/Mood)





```mermaid
 classDiagram
    class Mood
    click Mood href "../Mood/"
      Internal <|-- Mood
        click Internal href "../Internal/"
      
      
```





## Inheritance
* [Internal](Internal.md)
    * **Mood**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Mood](https://w3id.org/lmodel/dpv/pd/Mood) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Mood




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Mood |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Mood |
| native | pd:Mood |
| exact | dpv_pd:Mood, dpv_pd_owl:Mood |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Mood
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Mood
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about mood
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Mood
exact_mappings:
- dpv_pd:Mood
- dpv_pd_owl:Mood
is_a: Internal
class_uri: pd:Mood

```
</details>

### Induced

<details>
```yaml
name: Mood
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Mood
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about mood
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Mood
exact_mappings:
- dpv_pd:Mood
- dpv_pd_owl:Mood
is_a: Internal
class_uri: pd:Mood

```
</details></div>