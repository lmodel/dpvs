---
search:
  boost: 10.0
---

# Class: PrivacyPreference 


_Information about privacy preferences_



<div data-search-exclude markdown="1">



URI: [pd:PrivacyPreference](https://w3id.org/lmodel/dpv/pd/PrivacyPreference)





```mermaid
 classDiagram
    class PrivacyPreference
    click PrivacyPreference href "../PrivacyPreference/"
      Preference <|-- PrivacyPreference
        click Preference href "../Preference/"
      
      
```





## Inheritance
* [Internal](Internal.md)
    * [Preference](Preference.md)
        * **PrivacyPreference**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:PrivacyPreference](https://w3id.org/lmodel/dpv/pd/PrivacyPreference) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Privacy Preference




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#PrivacyPreference |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:PrivacyPreference |
| native | pd:PrivacyPreference |
| exact | dpv_pd:PrivacyPreference, dpv_pd_owl:PrivacyPreference |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PrivacyPreference
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PrivacyPreference
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about privacy preferences
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Privacy Preference
exact_mappings:
- dpv_pd:PrivacyPreference
- dpv_pd_owl:PrivacyPreference
is_a: Preference
class_uri: pd:PrivacyPreference

```
</details>

### Induced

<details>
```yaml
name: PrivacyPreference
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PrivacyPreference
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about privacy preferences
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Privacy Preference
exact_mappings:
- dpv_pd:PrivacyPreference
- dpv_pd_owl:PrivacyPreference
is_a: Preference
class_uri: pd:PrivacyPreference

```
</details></div>