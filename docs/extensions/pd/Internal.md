---
search:
  boost: 10.0
---

# Class: Internal 


_Information about internal characteristics that cannot be seen or_

_observed_



<div data-search-exclude markdown="1">



URI: [pd:Internal](https://w3id.org/lmodel/dpv/pd/Internal)





```mermaid
 classDiagram
    class Internal
    click Internal href "../Internal/"
      Internal <|-- Authenticating
        click Authenticating href "../Authenticating/"
      Internal <|-- Emotion
        click Emotion href "../Emotion/"
      Internal <|-- KnowledgeBelief
        click KnowledgeBelief href "../KnowledgeBelief/"
      Internal <|-- Mood
        click Mood href "../Mood/"
      Internal <|-- Preference
        click Preference href "../Preference/"
      
      
```





## Inheritance
* **Internal**
    * [Authenticating](Authenticating.md)
    * [Emotion](Emotion.md)
    * [KnowledgeBelief](KnowledgeBelief.md)
    * [Mood](Mood.md)
    * [Preference](Preference.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Internal](https://w3id.org/lmodel/dpv/pd/Internal) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Internal




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Internal |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Internal |
| native | pd:Internal |
| exact | dpv_pd:Internal, dpv_pd_owl:Internal |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Internal
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Internal
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about internal characteristics that cannot be seen or

  observed'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Internal
exact_mappings:
- dpv_pd:Internal
- dpv_pd_owl:Internal
class_uri: pd:Internal

```
</details>

### Induced

<details>
```yaml
name: Internal
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Internal
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about internal characteristics that cannot be seen or

  observed'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Internal
exact_mappings:
- dpv_pd:Internal
- dpv_pd_owl:Internal
class_uri: pd:Internal

```
</details></div>