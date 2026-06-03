---
search:
  boost: 10.0
---

# Class: Preference 


_Information about preferences or interests_



<div data-search-exclude markdown="1">



URI: [pd:Preference](https://w3id.org/lmodel/dpv/pd/Preference)





```mermaid
 classDiagram
    class Preference
    click Preference href "../Preference/"
      Internal <|-- Preference
        click Internal href "../Internal/"
      

      Preference <|-- Favourite
        click Favourite href "../Favourite/"
      Preference <|-- Intention
        click Intention href "../Intention/"
      Preference <|-- Interest
        click Interest href "../Interest/"
      Preference <|-- Opinion
        click Opinion href "../Opinion/"
      Preference <|-- PrivacyPreference
        click PrivacyPreference href "../PrivacyPreference/"
      

      
```





## Inheritance
* [Internal](Internal.md)
    * **Preference**
        * [Favourite](Favourite.md)
        * [Intention](Intention.md)
        * [Interest](Interest.md)
        * [Opinion](Opinion.md)
        * [PrivacyPreference](PrivacyPreference.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Preference](https://w3id.org/lmodel/dpv/pd/Preference) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Preference




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Preference |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Preference |
| native | pd:Preference |
| exact | dpv_pd:Preference, dpv_pd_owl:Preference |
| related | svd:Preference |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Preference
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Preference
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about preferences or interests
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Preference
exact_mappings:
- dpv_pd:Preference
- dpv_pd_owl:Preference
related_mappings:
- svd:Preference
is_a: Internal
class_uri: pd:Preference

```
</details>

### Induced

<details>
```yaml
name: Preference
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Preference
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about preferences or interests
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Preference
exact_mappings:
- dpv_pd:Preference
- dpv_pd_owl:Preference
related_mappings:
- svd:Preference
is_a: Internal
class_uri: pd:Preference

```
</details></div>